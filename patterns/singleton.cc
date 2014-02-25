// A sample implementation of the Singleton design pattern in C++
// Verify that it compiles using g++ -c singleton.cc

class GPU {
public:
    static GPU& getInstance() {
        // A static variable declared within a static method like this is
        // guaranteed to be instantiated the first time this method is called
        // and guaranteed to have its destructor called when the program exits.
        static GPU instance;
        return instance;
    }
private:
    // constructor is declared private so user code cannot create a GPU object
    GPU() {
        // Initialize and allocate the GPU here...
    }
    ~GPU() {
        // Do any cleanup and de-allocation here...
    }
    // We declare the assignment and copy ctors but do not implement them so
    // the compiler will not allow code to use them.
    GPU(GPU const&);
    void operator=(GPU const&);
};
