/**
  * Created by YGYG on 2018/7/24.
  */
object temp {
  def main(args:Array[String]): Unit = {
    var a = List[Int](32, 32, 34, 45, 35, 32, 30)
    println("本周七天温度列表为：" + a)
    for (i <- Range(0, 6)) {
      if (i == 2) {
        println("星期三的温度为：" + a(i))
      }
    }
  }
}
