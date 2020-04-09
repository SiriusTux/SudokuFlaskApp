
// Game button
var restart = $('#brestart') // var restart  = document.querySelector('#brestart');
var start = $('#bstart')

// Grabs all squares
//squares = $('td'); // var squares = document.querySelectorAll('td');

// Grabs Grid by Row
var grid = $('table tr')

// Function that clears all squares
function clearBoard() {
  for (var i = 0; i < $('td').length; i++) {
    $('td').eq(i).text(''); // squares[i].textContent = '';
  }
}
restart.on('click', clearBoard); // restart.addEventListener('click', clearBoard);

function returnValue(rowIndex, colIndex){
  return grid.eq(rowIndex).find('td').eq(colIndex).html()
}

start.on('click', function(){
  console.log(returnValue(1,0))
})
