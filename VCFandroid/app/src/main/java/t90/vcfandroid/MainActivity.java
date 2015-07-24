package t90.vcfandroid;

import android.annotation.TargetApi;
import android.app.Activity;
import android.content.res.AssetFileDescriptor;
import android.database.Cursor;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Environment;
import android.os.Handler;
import android.provider.ContactsContract;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

import com.dd.CircularProgressButton;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;


public class MainActivity extends Activity {

    CircularProgressButton connect;
    String path;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        connect = (CircularProgressButton) findViewById(R.id.connect);

        final String vfile = "VCFeditorBKP.vcf";
        path = Environment.getExternalStorageDirectory().getAbsolutePath() + File.separator + vfile;
        File f = new File(path);
        if(f.exists()){
            f.delete();
        }

        new Handler().postDelayed(new Runnable() {
            @TargetApi(Build.VERSION_CODES.ICE_CREAM_SANDWICH_MR1)
            @Override
            public void run() {
              connect.callOnClick();
            }
        }, 1500);
        connect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                connect.setIndeterminateProgressMode(true);
                connect.setProgress(50);
                (new getVCF()).execute();
            }
        });
    }

    public class getVCF extends AsyncTask<Void, Integer, String> {

        @Override
        protected String doInBackground(Void... params) {
            Cursor phones = getApplicationContext().getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, null,null, null, null);
            phones.moveToFirst();
            int max = phones.getCount();
            for(int i =0;i<max;i++){
                int prog = (i+1)/max;
                String lookupKey =  phones.getString(phones.getColumnIndex(ContactsContract.Contacts.LOOKUP_KEY));
                Uri uri = Uri.withAppendedPath(ContactsContract.Contacts.CONTENT_VCARD_URI, lookupKey);
                AssetFileDescriptor fd;
                try{
                    fd = getApplicationContext().getContentResolver().openAssetFileDescriptor(uri, "r");
                    FileInputStream fis = fd.createInputStream();
                    byte[] buf = new byte[(int) fd.getDeclaredLength()];
                    fis.read(buf);
                    String VCard = new String(buf);
                    FileOutputStream mFileOutputStream = new FileOutputStream(path, true);
                    mFileOutputStream.write(VCard.toString().getBytes());
                    phones.moveToNext();
                    publishProgress(prog);
                }
                catch (Exception e1){
                    // TODO Auto-generated catch block
                    e1.printStackTrace();
                    publishProgress(-1);
                }

            }
            return "success";
        }

        @Override
        protected void onPostExecute(String status) {
            if(status.equalsIgnoreCase("success")){
                connect.setProgress(100);
                Log.d("VCFSTATUS", "success," + path);
                MainActivity.this.finish();
            }
            else {
                connect.setProgress(-1);
            }
        }
    }
}
