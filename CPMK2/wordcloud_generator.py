from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(df, product_name):
    all_text = " ".join(df["clean_comment"])
    wc = WordCloud(width=800, height=400, background_color="white").generate(all_text)

    plt.figure(figsize=(8, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Word Cloud untuk {product_name}", fontsize=16)
    plt.show()
