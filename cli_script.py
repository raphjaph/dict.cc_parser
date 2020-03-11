from translator import Dictionary, SUPPORTED_LANGUAGES
import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description="This can translate one word" \
        "into two words from different languages. Currently supports: {}". format(
        ", ".join(SUPPORTED_LANGUAGES)))

    parser.add_argument("input_language", choices=SUPPORTED_LANGUAGES.keys())
    parser.add_argument("output_language", choices=SUPPORTED_LANGUAGES.keys())
    parser.add_argument("secondary_output_language", choices=SUPPORTED_LANGUAGES.keys())
    parser.add_argument("word", type=str)
    parser.add_argument("--num_translations","-n", type=int, default=5)

    return parser.parse_args()

def run():

    args = parse_arguments()
    translations = Dictionary.translate(args.word, args.input_language, args.output_language, args.num_translations)

    secondary_translations = Dictionary.translate(args.word, args.input_language, args.secondary_output_language, args.num_translations)


    print(args.input_language + " -> " + args.output_language)
    for pair in translations:
        print(pair[0]+ ".........." + pair[1])
    print("\n")
    print(args.input_language + " -> " + args.secondary_output_language)
    for pair in secondary_translations:
        print(pair[0]+ ".........." + pair[1])



if __name__ == "__main__":
    run()