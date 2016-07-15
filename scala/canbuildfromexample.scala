import scala.collection.mutable.LinkedHashMap
import scala.collection.generic._
import collection.mutable.{Builder}
import language.higherKinds

object Demo {
  def combineValues[U, T[_]](pairs: Seq[(String, String)])
                            (implicit cbf: CanBuildFrom[T[U], U, T[U]]) : Seq[(String, T[U])] = {

       val result = LinkedHashMap[String, Builder[U, T[U]]]() ## Builder implements Growable trait which allows it to grow underlying collection without creating new opject.
       for ((name, value) ← pairs) {
           result.getOrElseUpdate(name, cbf()) += value.asInstanceOf[U] ## Apply method to canbuild from returns builder instance.
       }
       result map { case (k, v) ⇒ k → v.result } toList
  }
  def combineValues_old(pairs: Seq[(String, String)]): Seq[(String, Seq[String])] = {
    val result = LinkedHashMap[String, List[String]]()

    for ((name, value) ← pairs)
      result += name → (value :: result.getOrElse(name, Nil))

    result.toList
  }
}
object Driver {
def main (argd : Array[String]){
    import Demo._
    var su: Seq[(String, String)] = Seq(("Ram", "Hello"), ("Jai", "Bye"), ("Ram", "whatsupp"))
    println(combineValues_old(su))
    println(combineValues[String, Set](su))
  }
}
