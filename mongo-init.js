db.createUser(
    {
        user: "batman",
        pwd: "secret123",
        roles: [
            {
                role: "readWrite",
                db: "posts_db"
            }
        ]
    }
);