import java.util.Scanner;
import java.util.ArrayList;

public class Galleta {

    public static void main(String[] args) {

        //Declaracion e inst de un AL
        ArrayList<String> frases = new ArrayList<>();
        try (Scanner miTeclado = new Scanner(System.in)) {
            //Declaramos variables
            int indice, indice2, num1;

            //Inicialización del arraylist mediante la carga de Strings
            frases.add("Hoy tendras mucha suerte");
            frases.add("Hoy recibiras ese llamado");
            frases.add("Hoy encontraras dinero en la calle");
            frases.add("Hoy te prepararan tu comida favorita");
            frases.add("Sacaras un 10 en tu próximo examen");
            frases.add("Todo estara mas que bien");
            frases.add("Recibiras un regalo");
            frases.add("Recibiras un ascenso");
            frases.add("LLegaras a tu peso ideal sin hacer dieta");
            frases.add("Te encontraras una persona muy querida");
            frases.add("Pronto recibiras ese llamado esperado");
            frases.add("Cuidado con el auto");
            frases.add("Hoy no es un buen dia para jugar valo");

            //Proceso
            //Instruccion de salida entrada
            System.out.println("Introduce tu numero de la suerte");
            num1 = miTeclado.nextInt();

            //Utilizamos random
            indice = (int)Math.floor(Math.random()*num1);
            indice2 = (int)Math.floor(Math.random()*(frases.size()-1));

            //Construyo una estructura if
            if (indice >=0 && indice < frases.size()){
             System.out.println("Hoy la suerte te dice que... "+frases.get(indice));
            }else{
             System.out.println("Para tu numero de la suerte: "+frases.get(indice2));   
            }
        }

        System.out.println("*** Sucedera pronto hasta luego! ***");
    }    

}