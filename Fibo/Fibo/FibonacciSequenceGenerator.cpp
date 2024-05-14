#include "FibonacciSequenceGenerator.h"
#include <cassert>

FibonacciSequenceGenerator::FibonacciSequenceGenerator(const std::string& aID) noexcept
    : fID(aID), fPrevious(0), fCurrent(1) {}

const std::string& FibonacciSequenceGenerator::id() const noexcept {
    return fID;
}

const long long& FibonacciSequenceGenerator::operator*() const noexcept {
    return fCurrent;
}

FibonacciSequenceGenerator::operator bool() const noexcept {
    return hasNext(); 
}


void FibonacciSequenceGenerator::reset() noexcept {
    fPrevious = 0;
    fCurrent = 1;
}

bool FibonacciSequenceGenerator::hasNext() const noexcept {
    return fCurrent <= LLONG_MAX - fPrevious;
}

void FibonacciSequenceGenerator::next() noexcept {
    long long temp = fCurrent;
    fCurrent += fPrevious;
    fPrevious = temp;
}
