//metodo ramdon y programamos bucle for
public class metodoRandom {
    public static void main(String[] args) {
    
     //1- Metodo random
     //System.out.println(Math.random());  
    
     //2- Metodo random con un numero entero
     //System.out.println(Math.random()*18);
    
     //3-Vamos a utilizar un for para generar 10 numero aleatorios
    /*for(int i=0; i<10; i++){
     System.out.println(Math.random());
    }*/
    
     /*//4-Vamos a utilizar un for para generar 10 numero aleatorios y ahora multip una const
    for(int i=0; i<10; i++){
     System.out.println(Math.random()*21);
    }*/

    /*//5- Vamos a generar numeros en un rango entre el 15 y el 31
    for(int i=0; i<10; i++){
    System.out.println(Math.floor(Math.random()*(31-15)+15));
   }*/

    //7- Vamos a generar numeros en un rango entre el 15 y el 31

    for(int i=0; i<10; i++){
    int numRandom = (int)Math.floor(Math.random()*(31-15)+15);
    System.out.println(numRandom);
       }

}
}