create table Parents(
RollNo number(7),
Foreign Key(RollNo) references Students(RollNo),
Name varchar2(25),
FatherName varchar2(20),
MotherName varchar2(20),
FatherOccupation varchar2(16),
MotherOccupation varchar2(16),
Email varchar2(30),
MobileNo number(12)
)