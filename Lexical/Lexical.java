			    //Types of Tokens
				// 1)Keyword
				// 2)Identifiers
				// 3)operators
				// 4)constants
				// 5)Special Symbols
				// 6)String



import java.util.*;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.lang.*;
class Lexical{
	public static void main(String args[]) throws IOException
			{
   

				int ch;
				String program ="";
				
				FileReader fr=null;
				try{
					 fr = new FileReader("output.txt");		
				}catch(FileNotFoundException fe)
				{
					System.out.print("File Not Found!");
				}
	         
	         while ((ch=fr.read())!=-1) {
	              program = program + (char)ch; //Copying the contents of file to string
	         }
				 String [] arrOfStr = program.split(" ");
				 List <String> l =Arrays.<String>asList(arrOfStr);
				 ArrayList<String> tokens = new ArrayList<String> (l);
         		 System.out.print(tokens);


	           fr.close(); 
			}
}