---
title: How we Built an Automated Glossary for Namibian Legislation
date: 2019-09-02 20:24:00 +02:00
lead: How we used legislation-as-data to create an automated glossary to explore over
  3000 defined terms in Namibian law.
author: Greg Kempe
image: "/uploads/glossary.png"
extra_js:
- <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.min.js"></script>
- |-
  <script>
    $(function() {
      var canvas = document.getElementById('glossary-chart'),
          ctx = canvas.getContext('2d'),
          labels = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z'],
          values = [1, 235, 100, 293, 200, 143, 138, 76, 53, 136, 17, 8, 124, 171, 100, 79, 341, 10, 228, 295, 173, 53, 49, 59, 3, 1];

      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Entries',
            data: values,
            borderWidth: 0,
            backgroundColor: '#D04242',
          }]
        },
        options: {
          maintainAspectRatio: false,
          legend: {display: false},
          title: {
            display: true,
            text: 'Number of Glossary Entries',
          },
          scales: {
            yAxes: [{
              ticks: {
                precision: 0,
                beginAtZero: true,
              },
            }],
            xAxes: [{
              gridLines: {
                display: false,
              }
            }],
          },
        }
      });
    });
  </script>
---

Legislation often defines terms that have a specific meaning. For instance, Namibia’s [Criminal Procedure Act (Act 25 of 2004)](https://edit.laws.africa/documents/2509/) defines “charge” as “an indictment, charge sheet, summons or written notice”. These definitions are crucial for the correct interpretation of legislation. It is interesting to explore which Acts define which terms and how those definitions change over time.

Using the Namibian statutes in the Laws.Africa legislation commons, we’ve created a [glossary of more than 3000 defined terms and definitions](https://edit.laws.africa/places/na/labs/glossary).

The glossary is updated automatically and doesn’t require any human editors, thanks to the machine-friendly legislation in the Laws.Africa commons. We use machine learning to group together similar definitions to make the glossary simpler to work with.

As of the date of this post, there are 3086 terms defined in 297 Acts. The bulk (79%) of the terms are defined in only one Act, 14% in two or three Acts, and the remaining 7% of term are defined in four or more Acts.

<div class="p-relative my-3" style="height: 200px;">
  <canvas id="glossary-chart"></canvas>
</div>

## The curious case of “minister”

Some terms are defined in many different acts with widely varying definitions. This is the case with “minister”.

The term “minister” is defined in 220 Acts. This is a common term since many Acts legislate how the government minister responsible for a particular area (such as Finance or Health) should execute their duties and obligations. The definition in each Act will depend on the subject area being legislated.

For example, here are the definitions of “minister” that relate to Health and Social Services:

> “Minister” means the Minister of Health and Social Services;
> * [National Welfare Act, 1965](https://edit.laws.africa/documents/2486/)
> * [National Pensions Act, 1992](https://edit.laws.africa/documents/2421/)
> * [Hospitals and Health Facilities Act, 1994](https://edit.laws.africa/documents/2360/)
{:.bg-light .px-2 .pt-2 .border}

> “Minister” means the Minister responsible for Social Services;
> * [Social Work and Psychology Act, 2004](https://edit.laws.africa/documents/2615/)
{:.bg-light .px-2 .pt-2 .border}

> “Minister” means the Minister responsible for Health and Social Services;
> * [Namibia Institute of Pathology Act, 1999](https://edit.laws.africa/documents/2357/)
{:.bg-light .px-2 .pt-2 .border}

The glossary has detected that these definitions are all related to Health and Social Services, and has grouped them together. It also groups together definitions that are identical.

Here are the definitions related to Agriculture:

> “Minister” means the Minister responsible for agriculture;
> * [Plant Quarantine Act, 2008](https://edit.laws.africa/documents/2141/)
> * [Animal Health Act, 2011](https://edit.laws.africa/documents/2430/)
> * [Seeds and Seeds Varieties Act, 2018](https://edit.laws.africa/documents/2618/)
{:.bg-light .px-2 .pt-2 .border}

> “Minister” means the Minister of Agriculture;
> * [Land Tenure Act, 1966](https://edit.laws.africa/documents/2419/)
> * [Soil Conservation Act, 1969](https://edit.laws.africa/documents/2138/)
> * [Subdivision of Agricultural Land Act, 1970](https://edit.laws.africa/documents/2394/)
{:.bg-light .px-2 .pt-2 .border}

In all, there are 79 groups of related definitions of “minister”.

It’s interesting to notice a trend in the definition of “minister”. Before the 1990s, Acts almost always use the wording “the Minister **of X**”. From the late 1990s onwards, however, most Acts use the new wording “the Minister **responsible for X**”.

## How old are “youth”?

It’s also interesting to discover definitions that are only slightly different. One might assume that the definition of “youth” would be consistent across the legislation. However, these two Acts define “youth” slightly differently:

> “youth” means a young person aged from 16 to 35 years old.
> * [National Youth Council Act, 2009](https://edit.laws.africa/documents/2531/)
{:.bg-light .px-2 .pt-2 .border}

> “youth” means an individual aged between 16 and 30 years.
> * [National Youth Service Act, 2005](https://edit.laws.africa/documents/2533/)
{:.bg-light .px-2 .pt-2 .border}

Similarly, the definition of a “minor” for gambling-related purposes is someone under the age of 21, whereas for witness protection purposes it is someone under the age of 18.

> “minor” means a person who has not attained the age of 21;
> * [Lotteries Act, 2017](https://edit.laws.africa/documents/2603/)
> * [Gaming and Entertainment Control Act, 2018](https://edit.laws.africa/documents/2633/)
{:.bg-light .px-2 .pt-2 .border}

> “minor” means a person who is below the age of 18 years;
> * [Witness Protection Act, 2017](https://edit.laws.africa/documents/2323/)
{:.bg-light .px-2 .pt-2 .border}

Besides being a useful research tool, there are lots of other interesting oddities to be found when exploring legislation through the lens of defined terms.

## How we built the Glossary

The glossary is built and maintained automatically. As we add and amend new Acts on Laws.Africa, the platform automatically identifies defined terms, extracts their definitions, groups similar definitions together, and updates the glossary. So how does it do this?

### Identifying definitions

At Laws.Africa we markup legislation using Akoma Ntoso XML. Our platform searches for a definition by looking for a phrase such as ‘“X” means...’ and then marks that up using the Akoma Ntoso `<def>` and `<term>` tags. 

```xml
<p refersTo="#term-day">
  “<def refersTo="#term-day">day</def>” means the space of time between sunrise and sunset;
</p>
```

It’s straight-forward to then go through through all Acts and extract the `<def>` elements.

### Grouping similar definitions

Once we have the terms and their definitions, we can cluster similar definitions together using some simple machine learning.

First, we extract the text from the definitions, strip punctuation and numbers, and normalise whitespace.

```python
def defn_text(element):
    """ Extract plain text (without punctuation and numbers) from definition XML elements.
    """
    # join text elements with spaces, strip punctuation, and convert to lowercase
    text = remove_punctuation(' '.join(element.itertext()) or '').lower()
    # replace numbers with N
    text = num_re.sub(r'[0-9]+', 'N', text)
    return text


def remove_punctuation(text):
    # strip punctuation in unicode
    # https://stackoverflow.com/questions/11066400/remove-punctuation-from-unicode-formatted-strings
    punct_table = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))
    return text.translate(punct_table)

# map a list of definition elements to plain text
texts = [defn_text(e) for e in definitions]
```

Now, for each term, we need to determine which definition texts are similar. We do this by vectorising the text and calculating the cosine similarity between the vectors. This gives what is effectively the “distance” between every pair of definitions.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(texts)
distances = 1 - cosine_similarity(tfidf)
```

Finally, we use [agglomerative clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering) to group the terms based on these distances. This gives us a list of cluster labels, one for each definition.

```python
from sklearn.cluster import AgglomerativeClustering

clustering = AgglomerativeClustering(
    n_clusters=None, compute_full_tree=True, distance_threshold=0.3,
    affinity='precomputed', linkage='complete').fit(distances)
labels = clustering.labels_
```

We then use these cluster labels to show related definitions in the glossary.

## The power of Legislation as Data

Treating legislation as machine-friendly data makes it really simple to build and maintain this glossary automatically, something that would have taken weeks or months of research by humans. This is just a small example of what’s possible with the machine-friendly Laws.Africa legislation commons. It simplifies previously time-consuming tasks and opens up a range of possibilities.

You can explore an automated glossary for all countries and places we have in the [Laws.Africa commons](https://edit.laws.africa/). Choose a country, click "Insights" and then click "Glossary". For example, check out the glossary for [Namibian national Acts](https://edit.laws.africa/places/na/labs/glossary) or the glossary for the [City of Cape Town’s by-laws](https://edit.laws.africa/places/za-cpt/labs/glossary).

What will you build with machine-friendly legislation?
