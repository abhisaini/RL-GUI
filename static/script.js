// function that builds a grid in the "container"
var x_coord = 0, y_coord = 0, gridsz , prev_x = -1, prev_y = -1;
// #9c412e dark red
function createGrid(x) {
    for (var rows = 0; rows < x; rows++) {
        for (var columns = 0; columns < x; columns++) {
            // console.log(max_col);
            mycolor = 'rgb(' + (255 - myGrid[rows][columns]/max_col * 25) + ',' + (255 - myGrid[rows][columns]/max_col * 55) + ',' + (255 - myGrid[rows][columns]/max_col * 115) + ')';
            // console.log(typeof mycolor);
            $("#container").append("<div class='grid ' style = 'background-color:"+ mycolor+ "; '><p >" + myGrid[rows][columns] +"</p></div>");
        };
    };
    $(".grid").width(720/x);
    $(".grid").height(720/x);
    var mgt = (360/x - 10) + 'px';
    $('.grid').children().css({'margin-top':mgt});
	// console.log(document.getElementsByClassName('grid').length);

};

function clearGrid(){
    $(".grid").remove();
};


function refreshGrid(){
    var z = prompt("How many boxes per side?");
    clearGrid();
    createGrid(z);
};

function color(i, j, gridsize, color, gtype, m){
    // console.trace();
	var grid  = $(gtype) ;
	// console.log(gtype);
    if(gtype == ".grid"){
        if(color == '#98e778'){
            grid[i * gridsize + j].style.background = color ;
        }
        else{
            var inf = grid[i * gridsize + j].inf;
            if(!inf){
                grid[i * gridsize + j].inf = 0;
            }
            if (inf >= 2){
                grid[i * gridsize + j].style.background ="#1d578e";
            }
            else if (inf == 1){
                grid[i * gridsize + j].style.background = "#4487c7";
            }
            else{
                grid[i * gridsize + j].style.background = color ;

            }
            // if(col)
            // else{
                grid[i * gridsize + j].inf += 1;
            // console.log(grid[i * gridsize + j].inf );
            // }
        }
        // console.log("(",i,j,")",inf);
    }
    else {

        // console.log("GRID : ", grid.length, i, j, color);
        grid[i * gridsize + j].style.background = "#e6c889" ;

    }

    // grid[i * gridsize + j].style.backgroundColor = "red";
    // console.log(color);


    // grid[i * gridsize + j].classList.add("fa");
    // grid[i * gridsize + j].classList.add("fa-long-arrow-right");

    // console.log(grid);
    // grid[i * gridsize + j].append("");


}


function checkEnd() {
    if(x_coord == gridsz - 1 && y_coord == gridsz - 1){
        alert("Cannot move now, reached the end.");
        console.log("end");
        return 1;
    }
    return 0;
}


function moveUp() {
	if(y_coord == 0){
		alert("invalid move") ;
		console.log("invalid move");
	}
	else{
        if(!checkEnd()){
    		y_coord --;
            color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
    		color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
            prev_x = x_coord, prev_y = y_coord;
        }

	}
}

function moveDown() {
	if(y_coord == gridsz - 1){
		alert("invalid move") ;
		console.log("invalid move");
	}
	else{
        if(!checkEnd()){
		y_coord ++;
        color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
        color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
        prev_x = x_coord, prev_y = y_coord;
        }
    }
}

function moveRight() {
	if(x_coord == gridsz - 1){
		alert("invalid move") ;
		console.log("invalid move");
	}
	else{
        if(!checkEnd()){
		x_coord ++;
        color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
        color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
        prev_x = x_coord, prev_y = y_coord;	}
    }
}

function moveLeft() {
	if(x_coord == 0){
		alert("invalid move") ;
		console.log("invalid move");
	}
	else{
        if(!checkEnd()){
		x_coord --;
        color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
        color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
        prev_x = x_coord, prev_y = y_coord;	}
    }
}


$(document).ready(function() {
    // createGrid(16);

    // $(".grid").mouseover(function() {
    //     $(this).css("background-color", "black");
    //     });


	createGrid(gridsz);
    createGridO(gridsz);


	color(x_coord ,y_coord ,gridsz, "#98e778", ".grid");
    prev_x = 0, prev_y = 0;
    color(gridsz-1 ,gridsz-1 ,gridsz, "#ea8d7a", ".grid");
    color(0,0,gridsz, "#e6c889", ".gridO");
    color(gridsz-1, gridsz-1,gridsz, "#e6c889", ".gridO");


	Mousetrap.bind('up', function(e) {
		moveUp();
	});
	$("#up").click(function() {
		moveUp();
	});


	Mousetrap.bind('down', function(e) {
		moveDown();
	});
	$("#down").click(function() {
		moveDown();
	});

	Mousetrap.bind('right', function(e) {
		moveRight();
	});
	$("#right").click(function() {
		moveRight();
	});

	Mousetrap.bind('left', function(e) {
		moveLeft();
	});
	$("#left").click(function() {
		moveLeft();
        // console.log(typeof this);
	});

    makeActions(myacs);



    // Extras

    // var mgtmp = $("#footer").height() + 'px';
    // $("#containerO").css({'margin-bottom':mgtmp});
    // console.log($("#containerO").css);
    $("#containerO").hide();
    $("#right-foot").addClass("active");

    // moveRightO();
    // moveDownO();
    // $(".newGrid").click(function() {
    //     refreshGrid();
	//
    //     $(".grid").mouseover(function() {
    //     $(this).css("background-color", "black");
    //     });
	//
    // });
});



function switchOpt() {
    $("#container").hide();
    $("#controller").hide();
    $("#containerO").show();
    $("#left-foot").addClass("active");
    $("#right-foot").removeClass("active");

}

function switchMy() {
    $("#container").show();
    $("#controller").show();
    $("#containerO").hide();
    $("#left-foot").removeClass("active");
    $("#right-foot").addClass("active");

}
// document.getElementById('container').style.visiblity = "hidden";

// function mypath(){
// 	var grid  = document.getElementsByClassName('grid') ;
//
// }
