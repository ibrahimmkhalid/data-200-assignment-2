import pandas as pd
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS

def get_data(graph):
    df = pd.read_csv('./core/data/scrubbed.csv')

    df = df[df['country'] == 'us']
    df = df.dropna(subset=['state'])

    fig = None
    if graph == 1:
        df = df.groupby(['state']).count().reset_index()
        df = df[['state', 'datetime']].rename(columns={'datetime': 'count'})
        df['state'] = df['state'].str.upper()

        fig = px.choropleth(
            df,
            color='count',
            locations='state',
            locationmode="USA-states",
            scope="usa",
            color_continuous_scale="Blues",
            labels={'count': "#Sightings"}
        )
    else:
        df['comments'] = df['comments'].astype(str)
        wordcloud_str = ' '.join(df[df['comments'] != 'nan']['comments'])
        custom_stopword = ['saw','sky', 'quot', 'light', 'lights', 'object', 'objects', 'ufo', 'ufos', 'craft', 'crafts', 'seen']

        stopwords = set(STOPWORDS)
        stopwords.update(custom_stopword)

        wordcloud = WordCloud(
            stopwords=stopwords,
            background_color='white',
            width=1200,
            height=900
        ).generate(wordcloud_str)

        fig = px.imshow(wordcloud)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

    return fig