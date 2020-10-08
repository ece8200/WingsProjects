package com.example.demo.services;

import com.example.demo.models.Book;
import com.example.demo.models.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class BookService {

    @Autowired
    private BookRepository bookRepository;

    public List<Book> findAllBooks(){
        List<Book> books = new ArrayList<>();
        Iterable<Book> allBooks= bookRepository.findAll();
        for ( Book book : allBooks
             ) {
            books.add(book);
        }
        return books;
    }
}
