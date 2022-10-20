function tocify(content, toc) {
  var stack;
  var items = [];

  content.querySelectorAll("h1, h2, h3, h4, h5").forEach(function (heading) {
    var item = {
      type: heading.tagName,
      title: heading.innerText,
      id: heading.id,
      children: [],
    };

    // top level
    if (!stack) {
      items.push(item);
      stack = [item];

    } else {
      // find the best sibling for this entry; if the stack is at h3 and we have h2, find an h2 or h1
      while (stack.length > 0 && stack[stack.length - 1].type > heading.tagName) {
        stack.pop();
      }
      var top = stack[stack.length - 1];

      if (top.type == heading.tagName) {
        // siblings
        if (stack.length > 1) {
          stack[stack.length - 2].children.push(item);
        } else {
          items.push(item);
        }
        stack[stack.length - 1] = item;
      } else {
        // child
        top.children.push(item);
        stack.push(item);
      }
    }
  });

  toc.items = items;
}

window.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll("[data-tocify]").forEach(function(content) {
    tocify(content, document.querySelector(content.getAttribute("data-tocify")));
  });
});
