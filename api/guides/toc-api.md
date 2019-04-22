---
title: "API Guide: Using the Table of Contents API"
lead: "Using the Laws.Africa Table of Contents API in your application."
navbar_item: api
layout: api/docs
---

This guide will take you through how to use the Table of Contents (TOC) API, part of Laws.Africa's Content API. After reading this guide you will know:

* what the Table of Contents API is and why it's useful
* how to call the Table of Contents API
* how to integrate the Table of Contents into your website or application
* how to display the Table of Contents and link it to the text of a work
* how to use the Table of Contents to fetch a section, chapter or part of a work

# What is the Table of Contents API?

The Table of Contents (TOC) API is a JSON description of the hierarchy and structure of a work. It's useful for including a Table of Contents in your website or application, or for helping your users navigate or explore the structure of a work.

For example, here's a screenshot of the Table of Contents for [Cape Town's Animal By-law](https://openbylaws.org.za/za-cpt/act/by-law/2011/animal/eng/) generated using the TOC API:

![Table of Contents for Cape Town's Animal By-law](/uploads/api-guides/animal-bylaw-toc.png)

Here's an extract of the corresponding JSON from the Table of Contents API:

```json
"toc": [
  {
    "type": "preamble",
    "subcomponent": "preamble",
    "url": "https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/eng/main/preamble",
    "title": "Preamble",
    "component": "main"
  },
  {
    "heading": "Interpretation",
    "type": "chapter",
    "id": "chapter-1",
    "component": "main",
    "url": "https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/eng/main/chapter/1",
    "title": "Chapter 1 – Interpretation",
    "num": "1",
    "subcomponent": "chapter/1"
    "children": [
      {
        "heading": "Definitions",
        "type": "section",
        "id": "section-1",
        "component": "main",
        "url": "https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/eng/main/section/1",
        "title": "1. Definitions",
        "num": "1.",
        "subcomponent": "section/1"
      }
    ],
  },
]
```

There is rich information about each element in the Table of Contents, including a type, number, heading, well-formatted title and URL. Each element may also contain nested children. For example, a part or chapter may contain sections.

# Why the Table of Contents API is useful

The Table of Contents API simplifies the task of navigating the structure of a work, both for the user and programatically. It takes care of the complications of dealing with Akoma Ntoso, such as handling different legislative traditions, doing translations and formatting titles, so that you don't have to.

Use the Table of Contents API to:

* put a clickable Table of Contents alongside a work on a webpage
* help the user navigate the structure of a work
* fetch certain parts, chapters and sections of a work directly from the API

# How to fetch the TOC for a work

Fetch the Table of Contents for a work using the `/frbr-uri/toc.json` URL for the work, such as [https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/toc.json](https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/toc.json).

```bash
$ curl -H "Authorization: Token <YOUR_AUTH_TOKEN>" \
  https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/toc.json
```

The Table of Contents will change depending on the language and date of the work expression.
{:.alert.alert-info}

You can also find this URL in the work's `links` array:

```json
"links": [
  {
    "title": "Table of Contents",
    "rel": "toc",
    "mediaType": "application/json",
    "href": "https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/toc.json"
  },
]
```

[→ Table of Contents API Documentation](https://laws.africa/api/docs#table-of-contents)

### Legislative traditions

The TOC API automatically adapts to the local legislative tradition of a country. For example, in South African legislation the Section is the basic unit. In other traditions, the Paragraph or Article is the basic unit. Laws.Africa handles this for you and generates a Table of Contents that takes local tradition into account.

# Showing a Table of Contents alongside a work

The most common use of the Table of Contents API is to put a clickable Table of Contents alongside a work in a website. This helps the user understand the structure of the text and navigate to the sections that are most important to them.

We're going to add the Table of Contents as a series of nested `ul` and `li` elements, and each entry will be a clickable `a` element with a link to the matching portion of the text.

We're going to use three key attributes of a Table of Contents entry:

* `title` – a formatted title for this entry, combining `num` and `heading`;
* `id` – the ID of this element in the HTML body of the work returned by the Content API; and
* `children` – a list of sub-entries underneath this entry.

First, let's assume you have fetched the work's HTML content from the `/frbr-uri.html` Content API and it's already on your webpage along with an empty element for the TOC:

```html
<aside id="toc"></aside>
<article class="akoma-ntoso">(HTML from Content API goes here)</article>
```

Let's also assume we have fetched the Table of Contents JSON from the API, and stored it the variable `toc`.

Now we're ready to add the Table of Contents as HTML to the page:

```js
function makeToc(entries) {
  // the container for these entries
  var ul = document.createElement('ul');

  entries.forEach(function(entry) {
    var li = document.createElement('li'),
        a = document.createElement('a');

    // make a link such as <a href="#chapter-1">Chapter 1</a>
    a.innerText = entry.title;
    // the entry.id matches the corresponding HTML body element's ID attribute
    if (entry.id) a.setAttribute('href', '#' + entry.id);
    li.appendChild(a);
    ul.appendChild(li);

    // make nested lists for this entry's children
    if (entry.children) {
      li.appendChild(makeToc(entry.children));
    }
  });

  return ul;
}

// transform the table of contents into a UL element and add it to the page
var ulToc = makeToc(toc);
document.getElementById('toc').appendChild(ulToc);
```

Now you have a clickable Table of Contents alongside your HTML:


```html
<aside id="toc">
  <ul>
    <li> 
      <a>Preamble</a>
    </li>
    <li>
      <a href="#chapter-1">Chapter 1 – Interpretation</a>
      <ul>
        <li>
          <a href="#section-1">1. Definitions</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#chapter-2">Chapter 2 – Dogs</a>
      <ul>
        <li>
          <a href="#section-2">2. Restriction on number of dogs</a>
        </li>
        <li>
          <a href="#section-3">3. Dog registration and licensing</a>
        </li>
        ...
      </ul>
    </li>
  </ul>
</aside>
```

# Fetching only a section, chapter or part of a work

The Table of Contents API also makes it easier to fetch portions of a work, such as a particular chapter, part or section. You can do this by using the `url` attribute of the TOC entry. Not all entries have a URL, so be sure to check first.

In this example we'll fetch the portion of the [Cape Town's Animal By-law](https://openbylaws.org.za/za-cpt/act/by-law/2011/animal/eng/) chosen by the user. Again, we'll assume that the Table of Contents JSON has been fetched and stored in the `toc` variable.

We'll use the TOC to populate a `select` element and then respond to a change by loading the HTML into a `div`.

```html
<label>Choose a section:</label> <select id="toc-selector"></select>
<div id="section-content" class="akoma-ntoso"></div>
```

```js
var select = document.getElementById('toc-selector');

// transform the TOC into options in a select
function makeTocSelect(entries) {
  entries.forEach(function(entry) {
    if (entry.url) {
      var option = document.createElement('option');
      option.innerText = entry.title;
      option.value = entry.url;
      select.appendChild(option);
    }

    // include entries for this entry's children
    if (entry.children) {
      makeTocSelect(entry.children);
    }
  });
}

// selection changed, load the HTML
function selectionChanged(e) {
  var xhr = new XMLHttpRequest(),
      container = document.getElementById('section-content'),
      url = e.target.value + '.html',
      // get your API token from https://edit.laws.africa/accounts/profile/api/
      apiToken = 'YOUR API TOKEN';

  xhr.open('GET', url);
  xhr.setRequestHeader('Authorization', 'Token ' + apiToken);
  xhr.onload = function() {
    if (xhr.status === 200) {
      container.innerHTML = xhr.responseText;
    } else {
      container.innerText = 'Request failed. Returned status of ' + xhr.status;
    }
  };
  xhr.send();
}

// fetch content when the selection changes
select.addEventListener('change', selectionChanged);

// build the select options
makeTocSelect(toc);
```

#### Live Demo

You need to get your API token from [https://edit.laws.africa/accounts/profile/api/](https://edit.laws.africa/accounts/profile/api/)
to use this demo.
{:.alert.alert-info}

<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/laws-africa/indigo-web@2.0.0/css/akoma-ntoso.min.css">

<div class="border p-2">
  <div class="row mb-3">
    <div class="col-md-6">
      <input type="text" class="form-control" id="api-token" placeholder="Enter your API token" onkeyup="loadToc();">
    </div>
  </div>

  <label>Choose a section:</label> <select id="toc-selector"></select>
  <div id="section-content" class="akoma-ntoso"></div>
</div>

<script>
var toc = [];
var select = document.getElementById('toc-selector');

function loadToc() {
  var apiToken = document.getElementById('api-token').value;
  if (apiToken && apiToken.length == 40 && toc.length == 0) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/toc.json');
    xhr.setRequestHeader('Authorization', 'Token ' + apiToken);
    xhr.onload = function() {
      if (xhr.status === 200) {
        toc = JSON.parse(xhr.response).toc;
        makeTocSelect(toc);
      }
    }
    xhr.send();
  }
}

// transform the TOC into options in a select
function makeTocSelect(entries) {
  entries.forEach(function(entry) {
    if (entry.url) {
      var option = document.createElement('option');
      option.innerText = entry.title;
      option.value = entry.url;
      select.appendChild(option);
    }

    // include entries for this entry's children
    if (entry.children) {
      makeTocSelect(entry.children);
    }
  });
}

// selection changed, load the HTML
function selectionChanged(e) {
  var xhr = new XMLHttpRequest(),
      container = document.getElementById('section-content'),
      url = e.target.value + '.html',
      // get your API token from https://edit.laws.africa/accounts/profile/api/
      apiToken = document.getElementById('api-token').value;

  xhr.open('GET', url);
  xhr.setRequestHeader('Authorization', 'Token ' + apiToken);
  xhr.onload = function() {
    if (xhr.status === 200) {
      container.innerHTML = xhr.responseText;
    } else {
      container.innerText = 'Request failed. Returned status of ' + xhr.status;
    }
  };
  xhr.send();
}

// fetch content when the selection changes
select.addEventListener('change', selectionChanged);

// we build the select options above, once the API token is entered
// makeTocSelect(toc);
</script>
