create table Section(
CollegeID number(7) primary key,
RollNo number(7),
Foreign key(RollNo) references Students(RollNo),
Name varchar2(25),
TeacherName varchar2(30),
ClassStartDate date,
ClassEndDate date
)
