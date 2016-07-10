// global variable for handling the tasks
var tasks = [];


/**
 * Handler for document ready event
 */
$(document).ready(function(){
    // handler for click event on Add new task button
    $('button#btn-add').on('click', function(){
        var text = $('input#description').val();
        if(text.trim().length == 0){
            return;
        }

        var task = new Task(text);
        $('ul#tasks').append(task.toHtml());
        $('input#description').val('');

        // update local tasks list and localStorage
        tasks.push(task);
        localStorage.tasks = JSON.stringify(tasks);
    });

    $('input').on('keypress', function(event){
        if(event.which == 13){  // if ENTER was pressed
            console.log('changed');
            console.log($('input#description').val());
        }
    });

    // handler for click event on Show All tasks button
    $('button#btn-show-all').on('click', function(){
        $('ul#tasks li').show();
    });

    // handler for click event on Show Active tasks button
    $('button#btn-show-active').on('click', function(){
        $('ul#tasks li[data-active=false').hide();
        $('ul#tasks li[data-active=true').show();
    });

    // handler for click event on Show Completed tasks button
    $('button#btn-show-completed').on('click', function(){
        $('ul#tasks li[data-active=false').show();
        $('ul#tasks li[data-active=true').hide();
    });

    // handler for click event on Clear Completed tasks button
    $('button#btn-clear-completed').on('click', function(){
        var toRemove = [];
        tasks.forEach(function(task, index, array){
            if(task.active == false){
                toRemove.push(index);
            }
        });
        console.log(toRemove);

        toRemove.forEach(function(item, index, array){
            tasks.splice(item, 1);
        });

        localStorage.tasks = JSON.stringify(tasks);

        // remove all completed tasks
        $('ul#tasks li[data-active=false').remove();
    });


    // render todolist
    if(localStorage.getItem('tasks') != null){
        var lsTasks = JSON.parse(localStorage.tasks);

        for(i in lsTasks){
            var task = new Task(lsTasks[i].description, lsTasks[i].active, lsTasks[i].id);
            tasks.push(task);
            $('ul#tasks').append(task.toHtml());
        }
    }
});


/**
 * Task constructor
 *
 * Creates new task based on it's description
 * @param description task description
 * @param active true, if task is still active, false otherwise (default is true)
 * @param id task id. if not set (null), id will be generated
 */
function Task(description, active = true, id = null){
    this.description = description;
    this.active = active;

    if(id == null){
        // uuid generator stolen from here: 
        // http://stackoverflow.com/questions/105034/create-guid-uuid-in-javascript
        this.id = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) { var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8); return v.toString(16); });
    }else{
        this.id = id;
    }
}


/**
 * Returns task as HTML element
 */
Task.prototype.toHtml = function(){
    var element = $('<li>')
        .attr('data-id', this.id)   // set task id
        .attr('data-active', this.active);  // set active state

    // set active/inactive
    if(this.active == false){
        element.html('<del>' + this.description + '</del>');
    }else{
        element.text(this.description);
    }

    // handle click event by changing it's state
    element.on('click', function(){
        var taskId = $(this).attr('data-id');

        // get task from tasks list
        for(var i = 0; i < tasks.length; i++){
            var task = tasks[i];
            if(task.id == taskId){
                // update the model
                task.active = !task.active;
                localStorage.tasks = JSON.stringify(tasks);
                
                // update the active attribute
                $(this).attr('data-active', task.active);

                // update the view
                if(task.active){
                    $(this).html(task.description);
                }else{
                    $(this).html('<del>' + task.description + '</del>');
                }

                break;
            }
        }
    });

    return element;
}
