import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re

nltk.download('stopwords')

LANGUAGE = "german"


class LegalTextSummarizer:
    """
    🧑‍⚖️ LegalTextSummarizer: Your tireless legal assistant for big cases! 📚

    This class helps you summarize extensive legal texts, like a dedicated legal assistant
    who can efficiently process large case files and extract the most crucial points.

    It's designed to handle substantial legal documents, making it perfect for summarizing
    entire law books or lengthy court decisions.
    """

    def __init__(self):
        self.stop_words = set(stopwords.words(LANGUAGE))

    @staticmethod
    def simple_sentence_tokenize(text):
        """
        ✂️ Divide and conquer the legal tome!

        This method breaks down the massive legal text into manageable sentences,
        like dividing a thick law book into individual pages for easier reading.

        Args:
            text (str): The voluminous legal text to be segmented.

        Returns:
            list: A list of sentence strings, each representing a 'page' of our law book.
        """
        sentences = re.findall(r'(§\s*\d+[^.!?\n]+|\(\d+\)[^.!?\n]+|[^.!?\n]+[.!?])', text)
        return [s.strip() for s in sentences if s.strip()]

    @staticmethod
    def simple_word_tokenize(text):
        """
        🔍 Catalog every word in the legal library!

        This method identifies all individual words, similar to creating an index
        for a massive legal library.

        Args:
            text (str): The text to be indexed.

        Returns:
            list: All words found in the text, like a comprehensive library index.
        """
        return re.findall(r'\w+', text.lower())

    def summarize_legal_text(self, text, num_sentences=10):
        """
        🎭 Craft a concise legal brief from a mountain of documents!

        This method distills a vast legal text into a succinct summary, much like
        how a skilled lawyer might prepare a brief executive summary of a complex case.

        Args:
            text (str): The extensive legal text, our complete case file.
            num_sentences (int): Desired length of the summary, like the page limit on a legal brief.

        Returns:
            str: A concise summary of the legal text, ready for quick review by a busy judge!
        """
        sentences = self.simple_sentence_tokenize(text)

        # Count word frequencies, like tallying the most cited precedents
        words = [word for sentence in sentences for word in self.simple_word_tokenize(sentence)
                 if word not in self.stop_words]
        word_frequencies = FreqDist(words)

        # Score sentences, like rating the importance of each piece of evidence
        sentence_scores = {}
        for i, sentence in enumerate(sentences):
            for word in self.simple_word_tokenize(sentence):
                if word in word_frequencies:
                    if i not in sentence_scores:
                        sentence_scores[i] = word_frequencies[word]
                    else:
                        sentence_scores[i] += word_frequencies[word]

        # Select top-scoring sentences, like choosing the most compelling arguments
        summary_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
        summary_indices.sort()  # Maintain chronological order, like preserving the case timeline

        # Construct the final summary, ensuring each major section (like chapters in a law book) is represented
        final_summary = []
        current_section = None
        for i in range(len(sentences)):

            if sentences[i].startswith('§'):
                current_section = sentences[i]

            if i in summary_indices:

                if current_section and (not final_summary or not any(s.startswith(current_section) for s in final_summary)):
                    final_summary.append(current_section + ':')

                if not sentences[i].startswith('§'):
                    # Ensure complete thoughts, like making sure each argument is fully presented
                    if sentences[i].startswith(('wenn', 'sonst')):
                        j = i - 1
                        while j >= 0 and not sentences[j].endswith(','):
                            j -= 1
                        if j >= 0:
                            final_summary.append(sentences[j] + ' ' + sentences[i])
                    else:
                        final_summary.append(sentences[i])

        # Polish the final summary, like proofreading the final brief
        final_summary = [s[0].upper() + s[1:] + ('.' if not s.endswith('.') else '') for s in final_summary]
        final_summary = [re.sub(r':\.', ':', s) for s in final_summary]

        return ' '.join(final_summary)
