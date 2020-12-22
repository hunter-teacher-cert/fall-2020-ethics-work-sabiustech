import java.util.ArrayList;
class Main {

  public static void main(String[] args) {
    //Set up Model
    ArrayList<Student> students = Setup.generateStudents();
    ArrayList<School> schools = Setup.generateSchools();

    System.out.println("\nStudents' Ranked Choices");
    for(Student s: students)
    {
      s.printRankedChoices();
    }


    System.out.println("\nSchools' Ranked Choices");
    for(School s: schools)
    {
      s.printRankedChoices();
    }

    System.out.println("\nEach School may accept 3 students.\nIn each round a provisional match is made.\nIt is updated every round to ensure stable matches.");

    Match.match(students, schools);

  }//end main
}//end class
