package com.cloudwick.kafka.java;

import java.util.Optional;

public interface TestInheri {
  default Boolean getValue () {
    return Boolean.FALSE;
  }
}


class Check implements TestInheri {

  Boolean check = null;
  @Override
  public Boolean getValue() {
    return  this.check;
  }

  public static void main (String arg[]) {
    TestInheri c = new Check();
    System.out.println(Optional.ofNullable(c.getValue()).orElse(Boolean.FALSE));
  }
}