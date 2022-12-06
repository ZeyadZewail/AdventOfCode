const {readFileSync, promises: fsPromises} = require('fs');

function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');
  
    const arr = contents.split(/\r?\n/);
  
    return arr;
  }

let file = syncReadFile('4.txt');
let pulls = file[0].split(',').map(num => parseInt(num, 10));
let boards = file.slice(2);

//console.log(pulls);

let counter = 1;
let temp = []


for(let i of boards){
    if(i == ""){
        continue;
    }

    if(counter == 1){
        temp[temp.length] = []
    }
    
    newI = i.trim().split(' ').filter(item => { return item != ''}).map(num => parseInt(num, 10));


    temp[temp.length-1].push(newI);

    counter++;

    if(counter == 6){
        counter = 1
    }
}


boards = temp
//console.log(boards)

//////////////////////end of parse/////////////////////////

let mark = (board,winner) =>{

    for (let i = 0; i < board.length; i++) {
        board[i] = board[i].map(item => item == winner ? item.toString() : item )
      }


}

//mark(boards[0],57);

//console.log(boards[0])

let testBoard = [
    [ '57', '7', '8', '38', '23' ],
    [ '17', 96, 5, 12, 18 ],  
    [ '58', 45, 81, 89, 4 ],  
    [ '73', 51, 93, 32, 10 ], 
    [ '74', 50, 26, 0, 24 ]   
  ];



let checkRows = (board) => {

    for(let row of board){
        let counter = 0;
        for(let number of row){
            if(typeof number === 'string'){counter++;}
            if(counter == 5){return true;}
        }   
    }

    return false;
}

//console.log(checkRows(testBoard));

let checkColumns = (board) => {
    
    
    for(let i = 0;i < board.length; i++){
        let counter = 0;
        for(let row of board){
            if(typeof row[i] === 'string'){counter++;}
        }

        if(counter == 5){return true;}
        
    }

    return false;
}


//console.log(checkColumns(testBoard));

let checkBoard = (board) =>{
    return  checkColumns(board) || checkRows(board) ;
}

let unMarkedSum = (board) => {
    let sum = 0;
    for(let row of board){
        for(let number of row){
            if(typeof number != 'string'){sum += number;}
            
        }   
    }

    return sum;
}



let findAnswer = (pulls,boards) => {
    let latestWinner = undefined;
    let latestPull = undefined;
    for(let pull of pulls){
        for(let i = 0;i < boards.length;i++){
            mark(boards[i],pull);
            
            if(checkBoard(boards[i])){
                latestWinner = boards[i];
                latestPull = pull;
                boards[i] = [];
            }
        }
    }
    console.log(latestWinner);
    console.log(latestPull);
    console.log(unMarkedSum(latestWinner));
    return unMarkedSum(latestWinner) * latestPull;
}


console.log(findAnswer(pulls,boards))
