   -- Derek, Kellen, Thomas  
-- Test File

with Text_IO; use Text_IO; 

procedure Main is
   a : integer := 5
   b : integer := 10;
   c : integer := a+b;
   message: string := "This is a message!"; -- This is a comment
   input: String(1 .. 1);
   
begin
   Put_Line("Hello World!");
   Put_Line(integer'image(c));
   Put_Line(message);

   Put_Line("1+1 = ?");
   get(input);

   if input = "2" then
      Put_Line("Correct");
   else
      Put_Line("Wrong, 1+1 = 2");
   end if;
end Main;

--Errors
   --No ;
   Put_Line(c)

   --Mismatched Parenthesis
   Put_Line(x+(b+1);

   -- if keywords needs to be followed by then keyword
   if x = 5

   --Mismatched Quote
   Put_Line("hello)