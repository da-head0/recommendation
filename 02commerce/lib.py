import psycopg2
import psycopg2.extras
from IPython.display import Image, display, HTML

def executeQuery(query, params=()):
    arr = []
    with psycopg2.connect("dbname=fcrec user=postgres password=") as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            for r in cursor:
                arr.append(dict(r))
    return arr


def displayItemInRows(rows):
    html = ""
    for row in rows:
        item_no = row['item_no']
        item_name = row['item_name']
        url = 'http://fcrec.bunjang.io/img/' + row['image_name'] + '.jpg'
        html += f'<img src="{url}" width=170 style="display:inline-block" title="{item_no} {item_name}">'
    display(HTML(html))


def displayItemDetailInRows(rows):

    cols = ['session_id', 'event_timestamp', 'item_no', 'item_name', 'category1_name', 'category2_name', 'category3_name', 'price', 'brand_name']

    html = "<table><thead><tr><td>image</td>"
    for h in cols:
        html += f"<td>{h}</td>"
    html += "</tr></thead>"

    for row in rows:
        url = 'http://fcrec.bunjang.io/img/' + row['image_name'] + '.jpg'
        html += f'<tr><td><img src="{url}" width=200 style="display:inline-block"></td>'
        for h in cols:
            html += f'<td>{row[h]}</td>'
        html += "</tr>"
    html += "</table>"
    display(HTML(html))



