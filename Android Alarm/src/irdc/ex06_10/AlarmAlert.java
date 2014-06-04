package irdc.ex06_10;

/* import相关class */
import android.app.Activity;
import android.app.AlarmManager;
import android.app.AlertDialog;
import android.app.PendingIntent;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;

/* 实际跳出闹铃Dialog的Activity */
public class AlarmAlert extends Activity
{
  private static  AlarmAlert alarmAlert;
  @Override
  protected void onCreate(Bundle savedInstanceState)
  {
    super.onCreate(savedInstanceState);
    Intent intent1 = new Intent(AlarmAlert.this,naozhong.class);
    //启动AlarmMusicService
    startService(intent1);
    new AlertDialog.Builder(AlarmAlert.this).setIcon(R.drawable.clock)
        .setTitle("闹钟响了!!").setMessage("赶快起床吧!!!").setPositiveButton(
            "关掉他", new DialogInterface.OnClickListener()
            {
              public void onClick(DialogInterface dialog,
                  int whichButton)
              {
                Intent intent1 = new Intent(AlarmAlert.this,naozhong.class);
                //启动AlarmMusicService
                stopService(intent1);
                /* 关闭Activity */
                AlarmAlert.this.finish();
              }
            }).show();
  }
  public static AlarmAlert getInstance(){
    return alarmAlert;
  }
}
