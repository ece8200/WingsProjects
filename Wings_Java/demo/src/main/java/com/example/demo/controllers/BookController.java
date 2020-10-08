package com.example.demo.controllers;

import com.example.demo.models.Book;
import com.example.demo.services.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class BookController {

    @Autowired
    private BookService bookService;

   @GetMapping("/Allbooks")
    public List<Book> getAllBooks() {
        List<Book> books = new ArrayList<>();
        books=bookService.findAllBooks();
        return books;
    }
}
