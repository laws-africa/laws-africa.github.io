function tocify($content, $toc) {
  var stack;

  $toc.empty();

  $content.find('h1, h2, h3, h4').each(function(i, heading) {
    var li = document.createElement('li'),
        a = document.createElement('a'),
        top;

    a.href = '#' + heading.id;
    a.innerHTML = heading.innerHTML;
    li.appendChild(a);

    // top level
    if (!stack) {
      $toc.append(li);
      stack = [[heading.tagName, li.parentElement]];

    } else {
      // find sibling, stack is at h3 and we want h1
      while (stack.length > 0 && stack[stack.length-1][0] > heading.tagName) stack.pop();
      top = stack[stack.length-1];

      if (top[0] == heading.tagName) {
        // siblings
        top[1].appendChild(li);

      } else {
        // child
        // new sublist
        ul = document.createElement('ul');
        ul.className = 'list-unstyled ml-3';
        ul.appendChild(li);

        top[1].lastElementChild.appendChild(ul);
        stack.push([heading.tagName, ul]);
      }
    }
  });
}

$(function() {
  $('[data-tocify]').each(function(i, content) {
    tocify($(content), $(content.getAttribute('data-tocify')));
  });
});
