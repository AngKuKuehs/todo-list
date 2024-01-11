# todo-list
A simple todo list API that uses Flask and MongoDB.

# Database Schema
Collection: Person
Document:
```
{
    _id: str
    title: str
    completed: bool
}
```

# Notes
- MongoDB connection string must be added as an environmental variable before deployment.

e.g.
```
MONGODB_URI="mongodb+srv://<username>:<password>@cluster0.a1bc2de.mongodb.net/?retryWrites=true&w=majority"
```

- To run locally, enter
`
poetry run flask --app app.py run &
`
in the CLI in the root directory of the project.