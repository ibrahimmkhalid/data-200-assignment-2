## DATA - 200 | Assignment 2
#### Ibrahim Mansoor Khalid

The goal of this assignment was to create 2 unique charts and display them on a page using django.

Dataset source: https://www.kaggle.com/datasets/NUFORC/ufo-sightings

Technologies/Libraries used:
- Django: Used for hosting actual webpage
- Jupyter Notebook: Used to explore dataset in a sandbox
- Pandas: Used to import and prepare the data
- Plotly: Used to generate actual charts and return them to page
- WordCloud: Used to generate the wordcloud image
- HTMX: Used to perform basic data fetching and replacing
- TailWindCSS: Used to perform basic styling on page

Using the assignment as a basis, I explored some other technologies I was interested in, HTMX and 
TailWindCSS. The 'core' application is configured with 2 urls. The first url displays the index 
page, while the second 'api' url returns the HTML required to display a graph. The index page expects
some context from Django, this context is a list of graphs. Each of these graphs contains the title, 
text, and id of that graph. The id is required to get the correct graph from the api url.

TailWindCSS was the primary method for page styling as it allows extensive expression without requiring
heavy styling libraries or external files. All styles can be displayed inline with the actual HTML element

When the page fully loads, the HTMX "load" event is triggered, this sends a GET request to the backend
using the api url. The response from this api call is actually just an HTML string, which replaces the
div it was called from. This is because of the HTMX swap parameter. There is also the additional
delay modifier in the swap parameter. This delay is required to make sure that the swap visually occurs
only after all the required JavaScript has finished running. This ensures that the page layout does not
drastically change into an undesirable state.

When the api is called, a function call is made to the 'backend.py' file. The 'get_data' function is
responsible for reading in the csv, preparing the data, and creating the correct graph based on the 
input. If it is the choropleth map, it will group the dataset by state and get the count. This is then
given to the plotly express to build the map. If the api requests the wordcloud image, all the comments
are concatenated in a single string and passed to the WordCloud class. This is then generated into an
image object. This image is then passed to plotly express. For either case, the plotly express figure
returned to the original api function. When the figure is returned, it is converted to HTML and sent
in an HttpResponse to the frontend.