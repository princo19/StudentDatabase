create table Students(
RollNO number(7) primary key,
Name varchar2(25),
DOB date,
Gender varchar2(10) check(Gender in('Male','Female','Other')),
Address varchar2(40),
State varchar2(25),
Email varchar2(40),
MobileNo number(12)
)