var i = 0;
var j = "";


function addBook(Title=undefined, ISBN=undefined, Author=undefined, Vendor=undefined)
{
  if ((Title == undefined) || (ISBN == undefined) || (Author == undefined) || (Vendor == undefined))
  {
    var title = document.getElementById("Title").value;
    var isbn = document.getElementById("ISBN").value;
    var author = document.getElementById("Author").value;
    var vendor = document.getElementById("Vendor").value;
  }
  else
  {
    var title = Title;
    var isbn = ISBN;
    var author = Author;
    var vendor = Vendor;
  }
  var table = document.getElementById("book-table");
  var L = ["Title, ISBN, Author, Vendor"];
  var A = [title, isbn, author, vendor];
  var tr = document.createElement("tr");
  var td;
  var td_text;
  var td_class;
  var td_button;
  var td_parent;
  var td_value;
  
  for (i=0; i<A.length; i++)
  {
    td = document.createElement("td");
    
    td_text = document.createTextNode(A[i]);
    td.appendChild(td_text);
    
    td_class = document.createAttribute("class");
    td_class.value = "table-text";
    td.setAttributeNode(td_class);

    td_value = document.createAttribute("value");
    td_value.value = A[i];
    td.setAttributeNode(td_value);
    
    td_button = document.createAttribute("onclick");
    td_button.value = "getBookData(this)";
    td.setAttributeNode(td_button);
    
    td_parent = document.createAttribute("parent");
    td_parent.value = td_text;
    td.setAttributeNode(td_parent);
    
    tr.appendChild(td);
  }
  table.appendChild(tr);
}

function getBookData(Node)
{
  var tr = Node.parentNode;
  var j;
  var title = tr.children[0].innerHTML;
  var isbn = tr.children[1].innerHTML;
  var author = tr.children[2].innerHTML;
  var vendor = tr.children[3].innerHTML;
  
  document.getElementById("changeMe").innerHTML = tr.innerHTML;
  
  document.getElementById("Title").innerHTML = title;
  document.getElementById("ISBN").innerHTML = isbn;
  document.getElementById("Author").innerHTML = author;
  document.getElementById("Vendor").innerHTML = vendor;
}

function changeTitle()
{
  j = document.getElementById("Title").value;
  document.getElementById("Title").innerHTML = j;
}

function changeISBN()
{
  j = document.getElementById("ISBN").value;
  document.getElementById("ISBN").innerHTML = j;
}

function changeAuthor()
{
  j = document.getElementById("Author").value;
  document.getElementById("Author").innerHTML = j;
}

function changeVendor()
{
  j = document.getElementById("Vendor").value;
  document.getElementById("Vendor").innerHTML = j;
}


function getRndInteger(min, max)
{
    return Math.floor(Math.random() * (max - min + 1) ) + min;
}

function addRndBooks(x=1)
{
  for (i=0; i<x; i++)
  {
    addBook(RndName(), RndName(), RndName(), RndName());
  }
}

function RndBook()
{
  var names = ["", "", "", ""];
  for (j=0; j<4; j++)
  {
    names[j] = RndName();
  }
  return names;
}

function RndName()
{
  var abc = "abcdefghijklmnopqrstuvwxyz";
  var hold = "";
  for (i=0; i<getRndInteger(4, 10); i++)
  {
    hold = hold + abc[getRndInteger(0, 25)];
  }
  return hold;
}

//addRndBooks(3);
//document.getElementById("changeMe").innerHTML = RndName();

//addBook("A", "A", "A", "A");
//addBook("B", "B", "B", "B");
addBook(RndName(), RndName(), RndName(), RndName());
addBook(RndName(), RndName(), RndName(), RndName());
addBook(RndName(), RndName(), RndName(), RndName());
addBook(RndName(), RndName(), RndName(), RndName());
