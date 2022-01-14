import re
import string

from hungarian_stemmer.hungarian_stemmer import HungarianStemmer
from digital_twin_distiller.ml_project import PreProcessorAbstract

class PreprocessInput(PreProcessorAbstract):
    def run(self, input_data: dict):
        """

        :param input_data:
        :return:
        """
        text = input_data["text"]
        text = text.lower()
        text = self.cleaning_numbers(text)
        text = self.cleaning_stopwords(text)
        text = self.cleaning_punctuations(text)
        text = self.hungarian_stemmer_stem(text)
        input_data["text"] = text
        return input_data

    @staticmethod
    def cleaning_numbers(text: str) -> str:
        """
        Method for deleteing numeric numbers from str
        :param text: String for cleaning numeric numbers
        :return:
        """

        return re.sub("[0-9]+", "", text)

    @staticmethod
    def cleaning_stopwords(text: str) -> str:
        """
        Method for deleteing Hungarian stopwords from str
        :param text: String for cleaning stopwords
        :return:
        """
        stopwords = [
            "a",
            "ahogy",
            "ahol",
            "is",
            "aki",
            "akik",
            "akkor",
            "alatt",
            "által",
            "általában",
            "amely",
            "amelyek",
            "amelyekben",
            "amelyeket",
            "amelyet",
            "amelynek",
            "ami",
            "amit",
            "amolyan",
            "amíg",
            "amikor",
            "át",
            "abban",
            "ahhoz",
            "annak",
            "arra",
            "arról",
            "az",
            "azok",
            "azon",
            "azt",
            "azzal",
            "azért",
            "aztán",
            "azután",
            "azonban",
            "bár",
            "be",
            "belül",
            "benne",
            "cikk",
            "cikkek",
            "cikkeket",
            "csak",
            "de",
            "e",
            "eddig",
            "egész",
            "egy",
            "egyes",
            "egyetlen",
            "egyéb",
            "egyik",
            "egyre",
            "ekkor",
            "el",
            "elég",
            "ellen",
            "elő",
            "először",
            "előtt",
            "első",
            "én",
            "éppen",
            "ebben",
            "ehhez",
            "emilyen",
            "ennek",
            "erre",
            "ez",
            "ezt",
            "ezek",
            "ezen",
            "ezzel",
            "ezért",
            "és",
            "fel",
            "felé",
            "hanem",
            "hiszen",
            "hogy",
            "hogyan",
            "igen",
            "így",
            "illetve",
            "ill.",
            "ill",
            "ilyen",
            "ilyenkor",
            "ison",
            "ismét",
            "itt",
            "jó",
            "jól",
            "jobban",
            "kell",
            "kellett",
            "keresztül",
            "keressünk",
            "ki",
            "kívül",
            "között",
            "közül",
            "legalább",
            "lehet",
            "lehetett",
            "legyen",
            "lenne",
            "lenni",
            "lesz",
            "lett",
            "maga",
            "magát",
            "majd",
            "majd",
            "már",
            "más",
            "másik",
            "meg",
            "még",
            "mellett",
            "mert",
            "mely",
            "melyek",
            "mi",
            "mit",
            "míg",
            "miért",
            "milyen",
            "mikor",
            "minden",
            "mindent",
            "mindenki",
            "mindig",
            "mint",
            "mintha",
            "mivel",
            "most",
            "nagy",
            "nagyobb",
            "nagyon",
            "ne",
            "néha",
            "nekem",
            "neki",
            "nem",
            "néhány",
            "nélkül",
            "nincs",
            "olyan",
            "ott",
            "össze",
            "ő",
            "ők",
            "őket",
            "pedig",
            "persze",
            "rá",
            "s",
            "saját",
            "sem",
            "semmi",
            "sok",
            "sokat",
            "sokkal",
            "számára",
            "szemben",
            "szerint",
            "szinte",
            "talán",
            "tehát",
            "teljes",
            "tovább",
            "továbbá",
            "több",
            "úgy",
            "ugyanis",
            "új",
            "újabb",
            "újra",
            "után",
            "utána",
            "utolsó",
            "vagy",
            "vagyis",
            "valaki",
            "valami",
            "valamint",
            "való",
            "vagyok",
            "van",
            "vannak",
            "volt",
            "voltam",
            "voltak",
            "voltunk",
            "vissza",
            "vele",
            "viszont",
            "volna",
        ]

        stopwords = set(stopwords)
        # this converts all whitespace characters to spaces and removes stopwords from text
        return " ".join([word for word in str(text).split() if word not in stopwords])

    @staticmethod
    def cleaning_punctuations(text: str) -> str:


        english_punctuations = string.punctuation
        punctuations_list = english_punctuations

        translator = str.maketrans("", "", punctuations_list)
        return text.translate(translator)

    @staticmethod
    def hungarian_stemmer_stem(text : str) -> str:
        """

        """

        hunstem = HungarianStemmer()

        returnlist = list()
        for token in text.split(" "):
            result = hunstem.stem(token)
            asString = ""
            for item in result:
                asString = asString + " " + item
            returnlist.append(asString)

        return " ".join(returnlist).replace("  ", " ")
