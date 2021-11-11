<h2> DJANGO TODO API</h2>

<table>
<strong>Instructions to run in your machine:</strong>
<li>
    <code>pip install -r requirements.txt</code>
</li>
<li>
    <code>python manage.py migrate</code><br>
</li>
<li>
    <code>python manage.py createsuperuser</code><br>
</li>
<li>
    <code>python manage.py runserver</code><br>
</li>
</table>
<ol>
<li>
    <code>/api/v1/create-todo</code>
</li>    
<p>
    This url accepts a <strong>POST</strong> method with todo json<br>
    <code>todo:{id:auto_added_by_api,
                name:string,
                description:string,
                isComplete:boolean,
                date:auto_added_by_api}
    </code>
</p>
<li>
    <code>/api/v1/todos</code>
    <p>Accepts a <strong>GET</strong> method tha list all todos</p>
</li>
<li>
    <code>/api/v1/todo/todo.id</code>
    <p>Accepts <strong>GET,PUT,PATCH</strong> methods in a todo by its given ID</p>
</li>
</ol>

