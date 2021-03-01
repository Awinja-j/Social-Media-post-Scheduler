db.createUser(
    {
        user: "batman",
        pwd: "secret123",
        roles: [
            {
                role: "readWrite",
                db: "scheduler_db"
            }
        ]
    }
);