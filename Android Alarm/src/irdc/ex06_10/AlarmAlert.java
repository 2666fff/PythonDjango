package irdc.ex06_10;

/* import���class */
import android.app.Activity;
import android.app.AlarmManager;
import android.app.AlertDialog;
import android.app.PendingIntent;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;

/* ʵ����������Dialog��Activity */
public class AlarmAlert extends Activity
{
  private static  AlarmAlert alarmAlert;
  @Override
  protected void onCreate(Bundle savedInstanceState)
  {
    super.onCreate(savedInstanceState);
    Intent intent1 = new Intent(AlarmAlert.this,naozhong.class);
    //����AlarmMusicService
    startService(intent1);
    new AlertDialog.Builder(AlarmAlert.this).setIcon(R.drawable.clock)
        .setTitle("��������!!").setMessage("�Ͽ��𴲰�!!!").setPositiveButton(
            "�ص���", new DialogInterface.OnClickListener()
            {
              public void onClick(DialogInterface dialog,
                  int whichButton)
              {
                Intent intent1 = new Intent(AlarmAlert.this,naozhong.class);
                //����AlarmMusicService
                stopService(intent1);
                /* �ر�Activity */
                AlarmAlert.this.finish();
              }
            }).show();
  }
  public static AlarmAlert getInstance(){
    return alarmAlert;
  }
}
