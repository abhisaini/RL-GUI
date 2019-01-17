// function that builds a grid in the "container"
var tg;
var x_coord , y_coord, gridsz , prev_x , prev_y ;
var reward_total = 0.0;
var myPath = [];
var grid_cpy;
var endflag = 0;
var time_beg , time_end;
// #9c412e dark red
function createGrid(x) {
    for (var rows = 0; rows < x; rows++) {
        for (var columns = 0; columns < x; columns++) {
            // console.log(max_col);
            mycolor = 'rgb(' + (240 - myGrid[rows][columns]/max_col * 75) + ',' + (234 - myGrid[rows][columns]/max_col * 105) + ',' + (222 - myGrid[rows][columns]/max_col * 165) + ')';
            // console.log( mycolor);
            // $("#container").append("<div class='grid ' style = 'background-color:"+ mycolor+ "; '><p >" + myGrid[rows][columns] +"</p></div>");
            $("#container").append("<div class='grid ' style = 'background-color:"+ mycolor+ "; '></div>");
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
        console.log(i,j);
        grid[i * gridsize + j].style.background = "#e6c889" ;

    }

    // grid[i * gridsize + j].style.backgroundColor = "red";
    // console.log(color);


    // grid[i * gridsize + j].classList.add("fa");
    // grid[i * gridsize + j].classList.add("fa-long-arrow-right");

    // console.log(grid);
    // grid[i * gridsize + j].append("");


}

function submit_grid() {
    time_end = new Date();
    time_end = time_end.getTime();
    var time_elapse = Math.round((time_end - time_beg) / 1000) ;
    console.log(time_elapse);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           console.log( xhttp.responseText);
        }
    };
    var url = "/survey?gridsz=" + gridsz + "&&actions=" + JSON.stringify(myPath) + "&&time=" + time_elapse + "&&reward=" + reward_total + "&&scene=" + scene
        + "&&grid=" + JSON.stringify(grid_cpy) + "&&opt_action=" + JSON.stringify(myacs)
         + "&&user_name=" + user_name + "&&user_roll=" + user_roll + "&&tg=" + tg;
    // console.log(url);
    xhttp.open("GET", url , true);
    xhttp.send();

    alert("Cannot move now, reached the end.Exiting to previous page.");
    console.log("end");
    window.location = "/";
    return 1;
}

function checkEnd() {
    if (x_coord == x_end && y_coord == y_end && endflag > 0){
        alert("Cannot move now, reached the end.");
        console.log("end");
        return 1;
    }
    else if (x_coord == x_end && y_coord == y_end && endflag == 0 ) {
        endflag = 1;


        submit_grid();


    }
    return 0;
}


function moveUp() {
	if(y_coord == 0){
        console.log(y_coord, x_coord);
		alert("invalid move up") ;
		console.log("invalid move up");
	}
	else{
        if(!checkEnd()){
            myPath.push(0);
    		y_coord --;
            reward_total += myGrid[y_coord][x_coord] ;
            myGrid[y_coord][x_coord] = 0;
            // console.log(myGrid[y_coord][x_coord]);
            color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
    		color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
            prev_x = x_coord, prev_y = y_coord;
            checkEnd();
        }

	}
}

function moveDown() {
	if(y_coord == gridsz - 1){
		alert("invalid move down") ;
		console.log("invalid move down");
	}
	else{
        if(!checkEnd()){
            myPath.push(1);
    		y_coord ++;
            reward_total += myGrid[y_coord][x_coord] ;
	    myGrid[y_coord][x_coord] = 0;
            // console.log(myGrid[y_coord][x_coord]);
            color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
            color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
            prev_x = x_coord, prev_y = y_coord;
            checkEnd();
        }
    }
}

function moveRight() {
	if(x_coord == gridsz - 1){
		alert("invalid move right") ;
		console.log("invalid move right");
	}
	else{
        if(!checkEnd()){
            myPath.push(2);
    		x_coord ++;
            reward_total += myGrid[y_coord][x_coord] ;
	    myGrid[y_coord][x_coord] = 0;
            // console.log(myGrid[y_coord][x_coord]);
            color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
            color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
            prev_x = x_coord, prev_y = y_coord;
            checkEnd();
        }
    }
}

function moveLeft() {

	if(x_coord == 0){
		alert("invalid move left") ;
		console.log("invalid move left");
	}
	else{
        if(!checkEnd()){
            myPath.push(3);
    		x_coord --;
            reward_total += myGrid[y_coord][x_coord] ;
	    myGrid[y_coord][x_coord] = 0;
            // console.log(myGrid[y_coord][x_coord]);
            color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
            color(prev_y ,prev_x ,gridsz, "#81bdf6", ".grid");
            prev_x = x_coord, prev_y = y_coord;
            checkEnd();
        }
    }
}


$(document).ready(function() {
    // createGrid(16);

    // $(".grid").mouseover(function() {
    //     $(this).css("background-color", "black");
    //     });


	createGrid(gridsz);
    createGridO(gridsz);


	color(y_coord ,x_coord ,gridsz, "#98e778", ".grid");
    // console.log("aaa : ", y_coord ,x_coord);
    prev_x = x_coord, prev_y = y_coord;
    reward_total += myGrid[y_coord][x_coord];
    color(y_end ,x_end,gridsz, "#ea8d7a", ".grid");
    color(0,0,gridsz, "#e6c889", ".gridO");
    color(y_end, x_end,gridsz, "#e6c889", ".gridO");


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

    // makeActions(myacs);



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




var user_name, user_roll ;
function getInfo() {
    var form_modal = document.getElementById('myModal');
    form_modal.style.display = "none";
    var gridworld = document.getElementById('gridworld');
    ctd_timer();
    gridworld.style.display = "block";
    user_name = document.getElementById('user_name').value;
    user_roll = document.getElementById('user_roll').value;
    time_beg = new Date();
    time_beg = time_beg.getTime();

}
// document.getElementById('container').style.visiblity = "hidden";

// function mypath(){
// 	var grid  = document.getElementsByClassName('grid') ;
//
// }
