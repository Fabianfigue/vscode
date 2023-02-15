import java.io.*;
import java.io.IOException;


public class CrearArchivo {
    public static void main(String[] args) {

        //Declaracion e instansacion del objeto file con nombre del archivo
        File archivo = new File("misDatos.txt");

        //Creacion del objeto mediante el metodo createNewFile en un try-catch
        try{
            archivo.createNewFile();
            if(archivo.exists()){
                System.out.println("El archivo se ha creado correctamente");
            }else {
                System.out.println("No se ha podido crear el archivo");
            }
        }catch( IOException e1){
            System.out.println("Se ha producido un error" + e1);
        }
        
        //verificacion de permisos de escritura sobre el archivo 
        System.out.println("Verificacion de permisos de escrituras: " + archivo.setWritable(true));
    }
}