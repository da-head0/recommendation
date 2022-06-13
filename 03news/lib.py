import psycopg2
import psycopg2.extras
from IPython.display import HTML, display
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def executeQuery(query, params=()):
    arr = []
    with psycopg2.connect("dbname=fcrec user=postgres password=") as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if cursor.description is not None:
                for r in cursor:
                    arr.append(dict(r))
    return arr

def is_pos_to_extract(tagged):
    tag = tagged[1]
    if tag.startswith('NN') or tag.startswith('VB') or tag.startswith('JJ') or tag.startswith('RB'):
        return True
    return False

def is_not_blank(obj):
    return obj and type(obj) is str and obj.strip()
    
def get_news_html(news, max_abstract_len=300):
    abstract = news['abstract']
    if len(abstract) > max_abstract_len:
        abstract = abstract[:max_abstract_len] + '...'
    html = f'''
        <div style='display:inline-block;min-width:200px;max-width:200px;vertical-align: top;'>
            <h3><a href="{news['url']}">{news['title']}</a></h3>
            <span>{news['category1']} &gt {news['category2']}</span>
            <p>{abstract}</p>
        </div>
    '''
    return html

def show_news(news):
    display(HTML(get_news_html(news)))
    return

def get_news_with_word_weight_dic(news_id):
    res = executeQuery(f"select * from mind_train_news where id = '{news_id}'");

    news = {}

    news['title'] = res[0]['title']
    news['abstract'] = res[0]['abstract']
    news['category1'] = res[0]['category1']
    news['category2'] = res[0]['category2']
    news['url'] = res[0]['url']

    res = executeQuery(f"select * from mind_train_news_word_w where news_id = '{news_id}'");
    dt = {}
    for r in res:
        dt[r['word']] = r['w']

    news['word_vec'] = dt

    res = executeQuery(f"select * from mind_train_news_entity_w where news_id = '{news_id}'");
    dt = {}
    for r in res:
        dt[r['label']] = r['w']

    news['entity_vec'] = dt

    return news
    
def create_wordcloud(dt):
    wordcloud = WordCloud(width = 800,
        height = 400,
        background_color="white")
    wordcloud.generate_from_frequencies(dt)

    return wordcloud

def show_wordcloud(wordcloud):
    fig = plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.show()
    return
