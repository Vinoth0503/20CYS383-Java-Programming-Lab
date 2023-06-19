package com.amrita.jpl.cys21085.endsem;

import javax.swing.*;
import java.util.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
abstract class File {
    private String fileName;
    private long fileSize;

    public File(String fileName, long fileSize) {
        this.fileName = fileName;
        this.fileSize = fileSize;
    }

    public String getFileName() {
        return fileName;
    }

    public long getFileSize() {
        return fileSize;
    }
    public void displayFileDetails(){

    }
}


class Document extends File{
    private String documentType;

    public Document(String fileName, long fileSize, String documentType) {
        super(fileName, fileSize);
        this.documentType = documentType;
    }
    public String getDocumentType(){
        return documentType;
    }
}
class Image extends File{
    private String resolution;
    public Image(String fileName, long fileSize, String resolution){
        super(fileName,fileSize);
        this.resolution = resolution;
    }
    public String getResolution(){
        return resolution;
    }


}

class Video extends File{
    private String duration;
    public Video(String fileName,long fileSize,String duration){
        super(fileName,fileSize);
        this.duration = duration;
    }

    public String getDuration(){
        return duration;
    }


}
interface FileManager {
    void addFile(File file);
    void deleteFile(String fileName);
    void saveToFile();
    void loadFromFile();
    ArrayList<File> getFiles();
}

class FileManagerImpl implements FileManager{
    ArrayList<File> files;

    public FileManagerImpl(){
        files = new ArrayList<>();
    }

    @Override
    public void addFile(File file) {
        files.add(file);
    }

    @Override
    public void deleteFile(String fileName) {
        for (File file : files){
            if(file.getFileName().equals(fileName)){
                files.remove(file);
            }
        }
    }

    @Override
    public void saveToFile() {
        try{
            FileWriter writer = new FileWriter("filedetails.txt");
            for(File file:files){
                writer.write(file.getFileName()+" "+file.getFileSize()+" ");

            }


        }catch (IOException e){
            System.out.println("File could not be opened/created. check directory permissions.");
        }

    }

    @Override
    public void loadFromFile() {

    }

    @Override
    public ArrayList<File> getFiles() {
        return files;
    }
}
public class FileManagementSystemUI {
    FileManager fileManager;
    private DefaultTableModel tableModel;
    public void FileManagementSystemUI(){
        fileManager = new FileManagerImpl();
        tableModel = new DefaultTableModel();
        tableModel.addColumn("File Name");
        tableModel.addColumn("File Size");
        tableModel.addColumn("Type/Resolution/Duration");
    }

    public void GUI(){
        JFrame frame = new JFrame("21UCYS End Semester Assignment File Manager");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setLayout(new BorderLayout());

        JPanel inputPanel = new JPanel(new GridLayout(1,6));
        JLabel fileName = new JLabel("File Name: ");
        JTextField nameinput = new JTextField();
        JLabel fileSize = new JLabel("File Size: ");
        JTextField sizeinput = new JTextField();
        String[] items = {"Document", "Image", "Video"};
        JComboBox<String> dropdown = new JComboBox<>(items);
        dropdown.setBounds(50, 50, 150, 30);

        frame.add(dropdown);

        inputPanel.add(fileName);
        inputPanel.add(nameinput);
        inputPanel.add(fileSize);
        inputPanel.add(sizeinput);

        JTable fileTable = new JTable(tableModel);
        JScrollPane scrollPane = new JScrollPane(fileTable);
        frame.add(scrollPane, BorderLayout.CENTER);

        JButton addButton = new JButton("Add File");
        JButton deleteButton = new JButton("Delete File");
        JButton displayButton = new JButton("Display All Files");
        JButton saveButton = new JButton("Save to File");
        JButton loadButton = new JButton("Load from File");
        JButton refreshButton = new JButton("Refresh");

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(addButton);
        buttonPanel.add(deleteButton);
        buttonPanel.add(displayButton);
        buttonPanel.add(saveButton);
        buttonPanel.add(loadButton);
        buttonPanel.add(refreshButton);

        frame.add(buttonPanel, BorderLayout.SOUTH);
        frame.setLayout(null);
        frame.setVisible(true);


    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                FileManagementSystemUI systemUI = new FileManagementSystemUI();
                systemUI.GUI();
            }
        });
    }
}