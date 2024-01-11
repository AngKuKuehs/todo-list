# todo-list
A simple todo list CRUD API that uses Flask and MongoDB Atlas. This project also makes use of poetry for dependency management.

# Document Schema
```
{
    _id: str
    title: str
    completed: bool
}
```

# Routes
## /get-all
Gets all exisitng reminders.

## /get-one
Given an id, returns the corresponding reminder.

## /add
Given a title, adds a reminder to the collection and returns the ObjectId.

## /update
Given an id and a title and/or completion status, updates the corresponding reminder.

## /remove
Given an id, removes the corresponding reminder in the collection.

# Deploying
## Render
1. On Render, select "new +" and create a new instance of a web service.
2. Select "Build and deploy from a Git repository".
3. Under "Public Git repository" enter the URL of this Git repository.
4. Add a unique name for the service, select the appropriate tier for the web app service. The other fields should be automtically filled.
5. Copy the connection string from your own MongoDB cluster and add it to the environmental variable under the name "MONGODB_URI".
6. Deploy the model. On the webservice page, select "Connect" and note down the IP addresses.
5. On MongoDB Atlas, add the IP addresses in the "Network Access Tabs".

After these steps, you should be able to send requests to the API.

# Notes
- MongoDB connection string must be added as an environmental variable before deployment.

e.g.
```
MONGODB_URI="mongodb+srv://<username>:<password>@cluster0.a1bc2de.mongodb.net/?retryWrites=true&w=majority"
```

- To run locally, enter
`
poetry run flask run
`
in the CLI in the root directory of the project.