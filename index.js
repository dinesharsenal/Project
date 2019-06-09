const mysql=require('mysql');
const express=require('express');
var app=express();
const bodyparser=require('body-parser');

app.use(bodyparser.json());



var mysqlConnection = mysql.createConnection({
	host:'localhost',
	user:'root',
	password:'',
	database: 'employeedb',
	multipleStatements: true
});

mysqlConnection.connect((err)=>{
	if(!err) console.log("DB Connection successful");
	else console.log("DB connection failed \n Error: "+JSON.stringify(err, undefined,2));
});
app.listen(3000, ()=>{
	console.log('Express server is running at port number 3000');
});

//employees
app.get('/employees', (req,res)=>{
	mysqlConnection.query('SELECT * FROM employee', (err, rows, fields)=>{
		if(!err) res.send(rows);
		else console.log(err);
	})
});

app.get('/employees/:id', (req,res)=>{
	mysqlConnection.query('SELECT * FROM employee WHERE EMPID=?',[req.params.id], (err, rows, fields)=>{
		if(!err) res.send(rows);
		else console.log(err);
	})
});

app.delete('/employees/:id', (req,res)=>{
	mysqlConnection.query('DELETE FROM employee WHERE EMPID=?',[req.params.id], (err, rows, fields)=>{
		if(!err) res.send("Deleted Successfully");
		else console.log(err);
	})
});
app.put('/employees/:id', (req,res)=>{
	let emp=req.body;

	var sql="SET @EMPID=?; SET @Name=?; SET @Empcode=?; SET @Salary=?;\
	CALL EmployeeAddOrEdit(@EMPID, @Name, @Empcode, @Salary);";
	mysqlConnection.query(sql, [emp.EMPID, emp.Name, emp.Empcode, emp.Salary], (err, rows, fields)=>{
		if(!err) {
			res.send("Updated Successfully");
		}
		else console.log(err);
	});
});

app.post('/employees', (req,res)=>{
	let emp=req.body;

	var sql="SET @EMPID=?; SET @Name=?; SET @Empcode=?; SET @Salary=?;\
	CALL EmployeeAddOrEdit(@EMPID, @Name, @Empcode, @Salary);";
	mysqlConnection.query(sql, [emp.EMPID, emp.Name, emp.Empcode, emp.Salary], (err, rows, fields)=>{
		if(!err) {
			res.send(rows);
		}
		else console.log(err);
	});
});



//Music



//employees
app.get('/albums', (req,res)=>{
	mysqlConnection.query('SELECT * FROM musicalbums', (err, rows, fields)=>{
		if(!err) res.send(rows);
		else console.log(err);
	})
});

app.get('/albums/:id', (req,res)=>{
	mysqlConnection.query('SELECT * FROM musicalbums WHERE AlbumID=?',[req.params.id], (err, rows, fields)=>{
		if(!err) res.send(rows);
		else console.log(err);
	})
});

app.delete('/albums/:id', (req,res)=>{
	mysqlConnection.query('DELETE FROM musicalbums WHERE AlbumID=?',[req.params.id], (err, rows, fields)=>{
		if(!err) res.send("Deleted Successfully");
		else console.log(err);
	})
});
app.put('/albums/:id', (req,res)=>{
	let emp=req.body;

	var sql="SET @AlbumID=?; SET @AlbumName=?; SET @ReleaseDate=?; SET @ArtistName=?; SET @Genre=?;\
	CALL musicalbumsAddOrEdit(@AlbumID, @AlbumName, @ReleaseDate, @ArtistName, @Genre);";
	mysqlConnection.query(sql, [emp.AlbumID, emp.AlbumName, emp.ReleaseDate, emp.ArtistName, emp.Genre], (err, rows, fields)=>{
		if(!err) {
			res.send("Updated Successfully");
		}
		else console.log(err);
	});
});

app.post('/albums', (req,res)=>{
	let emp=req.body;

	var sql="SET @AlbumID=?; SET @AlbumName=?; SET @ReleaseDate=?; SET @ArtistName=?; SET @Genre=?;\
	CALL musicalbumsAddOrEdit(@AlbumID, @AlbumName, @ReleaseDate, @ArtistName, @Genre);";
	mysqlConnection.query(sql, [emp.AlbumID, emp.AlbumName, emp.ReleaseDate, emp.ArtistName, emp.Genre], (err, rows, fields)=>{
		if(!err) {
			res.send(rows);
		}
		else console.log(err);
	})
});

//Courses

app.get('/courses', (req,res)=>{
	mysqlConnection.query('SELECT * FROM courses', (err, rows, fields)=>{
		if(!err) res.send(rows);
		else console.log(err);
	})
});

app.get('/courses/:id', (req,res)=>{
	mysqlConnection.query('SELECT * FROM courses WHERE CourseID=?',[req.params.id], (err, rows, fields)=>{
		if(!err) res.send(rows);
		else console.log(err);
	})
});

app.delete('/courses/:id', (req,res)=>{
	mysqlConnection.query('DELETE FROM courses WHERE CourseID=?',[req.params.id], (err, rows, fields)=>{
		if(!err) res.send("Deleted Successfully");
		else console.log(err);
	})
});
app.put('/courses/:id', (req,res)=>{
	let emp=req.body;

	var sql="SET @CourseID=?; SET @Name=?; SET @Instructor=?; SET @Duration=?;\
	CALL CourseAddOrEdit(@CourseID, @Name, @Instructor, @Duration);";
	mysqlConnection.query(sql, [emp.CourseID, emp.Name, emp.Instructor, emp.Duration], (err, rows, fields)=>{
		if(!err) {
			res.send("Updated Successfully");
		}
		else console.log(err);
	});
});

app.post('/courses', (req,res)=>{
	let emp=req.body;

	var sql="SET @CourseID=?; SET @Name=?; SET @Instructor=?; SET @Duration=?;\
	CALL CourseAddOrEdit(@CourseID, @Name, @Instructor, @Duration);";
	mysqlConnection.query(sql, [emp.CourseID, emp.Name, emp.Instructor, emp.Duration], (err, rows, fields)=>{
		if(!err) {
			res.send(rows);
		}
		else console.log(err);
	})
});