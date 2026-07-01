document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#add_item').addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
  });

  document.querySelector('#remove_item').addEventListener('click', function () {
    const list = document.querySelector('.my_list');
    if (list.lastChild) {
      list.removeChild(list.lastChild);
    }
  });

  document.querySelector('#clear_list').addEventListener('click', function () {
    const list = document.querySelector('.my_list');
    while (list.firstChild) {
      list.removeChild(list.firstChild);
    }
  });
});