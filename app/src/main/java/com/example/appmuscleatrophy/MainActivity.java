package com.example.appmuscleatrophy;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;



public class MainActivity extends AppCompatActivity {
    public TextView firstName;
    public TextView lastName;
    public static String[] random = {"Hi", "hello"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        firstName = findViewById(R.id.FirstName);
        lastName = findViewById(R.id.LastName);
    }
    public void ChangeName(View view){
       firstName.setText(random[0]);
       lastName.setText(random[1]);

    }
}