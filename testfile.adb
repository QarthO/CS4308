with Text_IO ; use Text_IO ;

procedure Main is
   x : integer := 5 ;
   y : integer := 10 ;
   z : integer := x + y ;
   message : string := "This is a message!" ;
begin
   Put_Line ( "Hello World!" ) ;
   Put_Line ( integer ' image ( z ) ) ;
   Put_Line ( message ) ;
end Main ;
