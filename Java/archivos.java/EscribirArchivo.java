import java.io.*;


public class EscribirArchivo {
    /**
     * @param args
     */
    public static void main(String[] args) {
        
    //Instanciacion de los objetos
        File archivo = new File("misDatos.txt");
        FileWriter archivoFw = new FileWriter(archivo, true); //true habilita a que los datos sean guardados en cola
    
        BufferedWriter archivoBw = new BufferedWriter(archivoFw);
    //bloque try-catch
        try{
    //Verificamos antes que el archivo tenga permiso de escritura
            System.out.println("verificacion del permiso de escr itura " + archivo.setWritable(true));

    //Variables
            String dni, nombre, apellido, sueldo, carga;

    //Hardcodeamos sabiendo que esto lo podemos optimizar con un bucle
            dni = "40936950";
            nombre = "Fabian";
            apellido = "Figueredo";
            sueldo = "60000";
    
            carga = dni + "," + nombre + "," + apellido + "," + sueldo;

    //Proceso de escritura del archivo
            archivoBw.write(carga); //Carga de datos en una linea
            ((BufferedWriter) archivo).newLine(); //Esto es para salto de linea
        }catch(FileNotFoundException e1){
            System.out.println("Archivo no encontrado");
        }catch(IOException e2){
            System.out.println("Lo siento no se puede operar con el archivo");

    }
        
}