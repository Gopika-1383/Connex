const {createPool} = require('mysql')
const pool = createPool({
    host: "localhost",
    user: "root",
    password: "Go@13082003",
    connectionLimit: 10
})
pool.query(`select * from user.details`,(name, mailid, password)=> {
    return console.log(password)
})
