import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io
import urllib.request

def create_chart(names: list, points: list) -> io.BytesIO:
    """Create chart with statistics"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    colors = ["#FF6B6B", "#4ECDC4", "#FFE66D", "#A8E6CF"]
    axes[0].bar(names, points, color=colors[:len(names)])
    axes[0].set_title("Статистика очков")
    axes[0].set_ylabel("Очки")

    axes[1].pie(points, labels=names, colors=colors[:len(names)], autopct="%1.1f%%")
    axes[1].set_title("Доли очков")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf

names_list =['Alina', 'Dmity', 'Valeriia']
scores = [7, 6, 5]

print(create_chart(names_list, scores))