package org.monads

/**
  * Created by ramsinha on 03/10/16.
  */


class PersonMonad {

}

//Copy with failure.

trait Monad [A] {
  def map [B] (f: A => B) : Monad [B]
  def flatMap[B] (f: A => Monad[B]) : Monad [B]
}


sealed trait Option[A]{
  def map [B] (f: A => B) : Option [B]
  def flatMap [B] (f : A => Option [B]) : Option [B]
}

// Some has some value 'a'
case class Some[A] (a: A) extends Option[A] {
  def map [B] (f : A => B ) : Option [B] = new Some(f(a))
  def flatMap [B] (f : A => Option [B] ) : Option [B] = f(a)
}

// None have absolutely no value.
case class None[A]  extends Option[A] {
  def map[B] (f: A => B) : Option [B] = new None
  def flatMap [B] (f : A => Option [B] ) : Option [B] = new None
}







