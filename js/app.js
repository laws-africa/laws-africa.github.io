function tocify($content, $toc) {
  var h2_ul,
      h1_li;

  $content.find('h1, h2').each(function(i, heading) {
    var li = document.createElement('li'),
        a = document.createElement('a');

    a.href = '#' + heading.id;
    a.setAttribute('data-title', heading.getAttribute('title') || heading.innerText);
    a.innerHTML = heading.innerHTML;
    a.className = 'toc-' + heading.tagName.toLowerCase() + ' toc-link';
    li.appendChild(a);

    if (heading.tagName == 'H1') {
      // h1
      h1_li = li;
      h2_ul = null;
      $toc.append(li);

    } else {
      // h2
      if (!h2_ul) {
        h2_ul = document.createElement('ul');
        h2_ul.className = 'toc-list-h2';
        h1_li.appendChild(h2_ul);
      }

      h2_ul.appendChild(li);
    }

  });
}

$(function() {
  $('[data-tocify]').each(function(i, content) {
    tocify($(content), $(content.getAttribute('data-tocify')));
  });
});
