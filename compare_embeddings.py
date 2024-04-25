from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator


def main():
    # Get embedding for a word.
    embedding_function = OpenAIEmbeddings()
    vector = embedding_function.embed_query("Bessma")
    

    # Compare vector of two words
    evaluator = load_evaluator("pairwise_embedding_distance")
    words = ("Ahmed", "girl")
    x = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    with open("output.txt", "w") as f:
        f.write(f"Vector for 'Bessma': {vector}")
        f.write(f"\n\n:")
        f.write(f"Vector length: {len(vector)}")
        f.write(f"\n\n:")
        f.write(f"Comparing ({words[0]}, {words[1]}): {x}")
    # print(f"Comparing ({words[0]}, {words[1]}): {x}")


if __name__ == "__main__":
    main()
